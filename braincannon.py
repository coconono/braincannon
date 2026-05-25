#!/usr/bin/env python3
"""
braincannon - A simple tool to post to Bluesky social media platform

Yeet your thoughts into the void without looking back.
"""

import sys
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from atproto import Client
from time import sleep


def load_config(config_path="config.yaml"):
    """Load configuration from YAML file"""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        required_fields = ['handle', 'app_password']
        for field in required_fields:
            if field not in config:
                raise ValueError(f"Missing required field: {field}")
        
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.", file=sys.stderr)
        print("Please create a config.yaml from config.yaml.example", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML configuration: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)


def post_to_bluesky(text, config, max_retries=3):
    """
    Post text to Bluesky with retry logic
    
    Args:
        text: The text to post
        config: Configuration dictionary with handle and app_password
        max_retries: Maximum number of retry attempts
    
    Returns:
        True if successful, False otherwise
    """
    if not text or not text.strip():
        print("Error: Cannot post empty text", file=sys.stderr)
        return False
    
    # Bluesky has a 300 character limit per post
    if len(text) > 300:
        print(f"Warning: Text is {len(text)} characters, Bluesky limit is 300", file=sys.stderr)
        print("Truncating to 300 characters...", file=sys.stderr)
        text = text[:300]
    
    client = Client()
    
    for attempt in range(max_retries):
        try:
            # Login to Bluesky
            client.login(config['handle'], config['app_password'])
            
            # Create the post
            response = client.send_post(text=text)
            
            print(f"✓ Successfully posted to Bluesky!")
            print(f"Post URI: {response.uri}")
            print(f"Post CID: {response.cid}")
            
            return True
            
        except Exception as e:
            attempt_num = attempt + 1
            if attempt_num < max_retries:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"Attempt {attempt_num} failed: {e}", file=sys.stderr)
                print(f"Retrying in {wait_time} seconds...", file=sys.stderr)
                sleep(wait_time)
            else:
                print(f"Error: Failed to post after {max_retries} attempts", file=sys.stderr)
                print(f"Last error: {e}", file=sys.stderr)
                return False
    
    return False


def main():
    parser = argparse.ArgumentParser(
        description='Post to Bluesky from the command line',
        epilog='Example: braincannon.py "Just had the best coffee ever!"'
    )
    
    parser.add_argument(
        'text',
        nargs='?',
        help='The text to post (or read from stdin)'
    )
    
    parser.add_argument(
        '-c', '--config',
        default='config.yaml',
        help='Path to configuration file (default: config.yaml)'
    )
    
    parser.add_argument(
        '-r', '--retries',
        type=int,
        default=3,
        help='Maximum number of retry attempts (default: 3)'
    )
    
    parser.add_argument(
        '-i', '--stdin',
        action='store_true',
        help='Read text from stdin'
    )
    
    args = parser.parse_args()
    
    # Get text from stdin or command line argument
    if args.stdin or not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    elif args.text:
        text = args.text
    else:
        parser.print_help()
        sys.exit(1)
    
    if not text:
        print("Error: No text provided to post", file=sys.stderr)
        sys.exit(1)
    
    # Load configuration
    config = load_config(args.config)
    
    # Post to Bluesky
    success = post_to_bluesky(text, config, max_retries=args.retries)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
