# Password Checker

A simple and efficient Python tool that evaluates the strength of passwords and checks if they have been compromised in any known data breaches. This tool uses a secure implementation to query the [Have I Been Pwned API](https://haveibeenpwned.com/) for password breaches without exposing your actual password.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Example](#example)
- [Dependencies](#dependencies)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)

## Features
- Check if your password has been compromised in any known data breaches.
- Uses the secure K-anonymity model when querying the Have I Been Pwned API.
- Works for multiple passwords in a single run.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kyton91/passwordChecker.git
   cd passwordChecker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script and pass your password(s) as arguments:
```bash
python password_checker.py <password1> <password2> ...
```

### Example Usage:
```bash
python password_checker.py P@ssw0rd123 weakpass 123456
```

## How It Works
The tool evaluates passwords using the following steps:
1. **Hashing the Password**:
   - The password is hashed using SHA1.
   - The first 5 characters of the hash are sent to the [Have I Been Pwned API](https://haveibeenpwned.com/).

2. **K-Anonymity Model**:
   - Only the hash prefix (first 5 characters) is shared with the API.
   - The API responds with hash suffixes and their breach counts.

3. **Leak Check**:
   - The tool compares the hash suffix of the input password with the API response.
   - If a match is found, it reports how many times the password has appeared in breaches.

## Example
```bash
> python password_checker.py P@ssw0rd123 weakpass
P@ssw0rd123 has been leaked 1200 times you should change it

weakpass has not been leaked yet
```

## Dependencies
This tool requires:
- Python 3.6+
- `requests` (for API calls)

You can install all dependencies with:
```bash
pip install -r requirements.txt
```

## Code Overview
The main components of the script are:

### Functions:
1. **`request_api_data(query_string)`**
   - Sends a GET request to the Have I Been Pwned API with the given hash prefix.
   - Handles errors if the response is invalid.

2. **`check_password(password)`**
   - Hashes the input password using SHA1.
   - Splits the hash into the first 5 characters (prefix) and the rest (suffix).
   - Calls `request_api_data` and checks for leaks using `get_passwords_leak_count`.

3. **`get_passwords_leak_count(hashes, hash_to_check)`**
   - Parses the API response to check if the password hash suffix exists.
   - Returns the breach count if found, otherwise returns 0.

4. **`main(args)`**
   - Iterates through passwords passed as command-line arguments.
   - Checks each password and prints the result.

### Execution:
The script is executed as follows:
```bash
sys.exit(main(sys.argv[1:]))
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the project.
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your branch and submit a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Author**: [Kyton91](https://github.com/kyton91)

Feel free to contact me with suggestions or feedback!
