# A client for interacting with digital ocean spaces
A collection of utility functions for working with DigitalOcean Spaces.

This package provides a set of functions for uploading, downloading, and deleting files from DigitalOcean Spaces.

## Installation
You can install `digitalocean_spaces_client` using pip:
```bash
pip install git+https://github.com/HamzaFa61/digitalocean_spaces_client
```
## Usage
To use the functions in `digitalocean_spaces_client`, you'll need to provide your DigitalOcean Spaces access key ID, secret access key, and endpoint URL. You can obtain these values from your DigitalOcean account settings.
```python
import boto3
import digitalocean_spaces_client

# Set your DigitalOcean Spaces credentials
SPACES_ACCESS_KEY_ID = 'your_access_key_id'
SPACES_SECRET_ACCESS_KEY = 'your_secret_access_key'
SPACES_ENDPOINT_URL = 'your_endpoint_url'

# Create a DigitalOcean Spaces client
spaces_client = digitalocean_spaces_client.get_spaces_client(
    region_name='nyc3',
    endpoint_url=SPACES_ENDPOINT_URL,
    key_id=SPACES_ACCESS_KEY_ID,
    secret_access_key=SPACES_SECRET_ACCESS_KEY
)

# Upload a file to your Space
with open('/path/to/local/file.jpg', 'rb') as file:
    url = digitalocean_spaces_client.upload_file(spaces_client, 'your_space_name', file)

# Delete a file from your Space
url = 'https://your_space_name.nyc3.digitaloceanspaces.com/path/to/file.jpg'
digitalocean_spaces_client.delete_file(spaces_client, 'your_space_name', url)
```
For more information on how to use each of the functions in digitalocean_spaces_client, see the docstrings in the source code.

## Contributing
Contributions are welcome! Please submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
