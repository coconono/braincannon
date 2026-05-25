# 🧠💥 braincannon

A very simple command-line tool to post to Bluesky social media platform. 

## What is this?

braincannon lets you yeet thoughts to Bluesky from your terminal.

I don't think you should really do this if you're a real poster in the modern era.

Basically a proof of concept how easily AP protocol gets botted. I did this with copilot.

## Features

- 🚀 Post text to Bluesky from command line
- 🔁 Automatic retry logic with exponential backoff
- 📝 Read from stdin or command-line arguments
- ⚙️ Simple YAML configuration
- 🔒 Secure credential management
- 🐍 Automatic Python environment setup

## Prerequisites

- Python 3.8 or higher
- A Bluesky account
- Bash-like shell (zsh and all the fancy supported)

## Installation

1. **Clone or download this repository**

2. **Set up your credentials**

   First, generate an app password from Bluesky:
   - Log into Bluesky
   - Go to: Settings → Privacy and Security → App Passwords
   - Click "Add App Password"
   - Give it a name (e.g., "braincannon")
   - Copy the generated password

3. **Create your config file**

   ```bash
   cp config.yaml.example config.yaml
   ```

   Edit `config.yaml` and add your credentials:

   ```yaml
   handle: "yourhandle.bsky.social"
   app_password: "your-app-password-here"
   ```

   ⚠️ **IMPORTANT**: Never commit `config.yaml` to version control!

4. **Make the launcher executable** (if not already)

   ```bash
   chmod +x braincannon.sh
   ```

## Usage

### Basic usage

Post a simple message:

```bash
./braincannon.sh "Just had the best coffee ever!"
```

### Read from stdin

Pipe text into braincannon:

```bash
echo "This is my thought" | ./braincannon.sh -i
```

Or use heredoc for multi-line (will be joined):

```bash
./braincannon.sh <<< "Quick thought from terminal"
```

### Using the Python script directly

If you prefer to manage the Python environment yourself:

```bash
python3 braincannon.py "Your message here"
```

### Command-line options

```bash
./braincannon.sh [OPTIONS] "text to post"

Options:
  -c, --config PATH     Path to config file (default: config.yaml)
  -r, --retries NUM     Max retry attempts (default: 3)
  -i, --stdin          Read text from stdin
  -h, --help           Show help message
```

### Examples

Post with custom config file:

```bash
./braincannon.sh -c ~/.config/bluesky.yaml "Hello world"
```

Set max retries:

```bash
./braincannon.sh -r 5 "This better work"
```

Create an alias for quick posting:

```bash
# Add to your ~/.zshrc or ~/.bashrc
alias yeet='~/scripts/braincannon/braincannon.sh'

# Then use it:
yeet "Short thought, big impact"
```

## How It Works

1. **braincannon.sh** - Launcher script that:
   - Creates a Python virtual environment (`.venv/`) on first run
   - Installs required dependencies automatically
   - Runs the Python script
   - Handles cleanup

2. **braincannon.py** - Main Python script that:
   - Loads credentials from `config.yaml`
   - Authenticates with Bluesky using AT Protocol
   - Posts your text
   - Retries on failure with exponential backoff

3. **config.yaml** - Your credentials (not in version control)

## Python Environment

The launcher script (`braincannon.sh`) automatically:

- Creates a virtual environment in `.venv/`
- Installs dependencies from `requirements.txt`
- Activates the environment before running
- Deactivates after completion

You don't need to manually manage the Python environment unless you want to.

### Manual Python environment setup

If you prefer to set up the environment yourself:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 braincannon.py "Your message"
deactivate
```

## Troubleshooting

### "config.yaml not found"

Make sure you've copied `config.yaml.example` to `config.yaml` and filled in your credentials.

### "Failed to post after N attempts"

- Check your internet connection
- Verify your credentials are correct
- Check if Bluesky is having service issues
- Try increasing retry attempts with `-r` flag

### "Text is too long"

Bluesky has a 300 character limit. The script will automatically truncate longer messages.

## Security Notes

- `config.yaml` contains sensitive credentials and should NEVER be committed to version control
- The `.gitignore` file is configured to exclude `config.yaml`
- App passwords are safer than using your main password
- You can revoke app passwords anytime from Bluesky settings

## Contributing

Contributions welcome! This is a simple tool, but if you have ideas:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

Ideas for enhancements:

- Support for images/media
- Multiple account management
- Scheduling posts
- Thread support
- Draft management
- Interactive mode

## License

Use it however you want. No warranty. Don't blame me if your posts are bad.

## Philosophy

Sometimes you just need to throw a thought into the void without the immediate feedback loop of social media. This tool is for those moments. Post and move on with your life.

---

*"Fire and forget" - The braincannon way* 🧠💥
