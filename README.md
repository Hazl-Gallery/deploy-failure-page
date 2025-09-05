# Deploy Failure Page

A simple one-page Docker app that displays deployment failure messages with customizable error text.

## Features

- Clean, professional failure page design with red error styling
- Support for both plain text and Markdown formatted failure messages
- Automatic timestamp display showing when the failure occurred
- Responsive design that works on all devices
- No-cache headers to prevent browser caching issues
- Easy to customize failure text via environment variables

## Quick Start

### 1. Build the Docker Image

```bash
docker build -t deploy-failure-page .
```

### 2. Run with Simple Text

```bash
docker run -d -p 8080:80 -e PORT=8080 -e FAILURE_TEXT="Deployment failed: Database connection error" deploy-failure-page
```

### 3. Access the Page

Visit `http://localhost:8080` to view the failure page.

## Usage Examples

### Simple Text Message
```bash
docker run -d -p 8080:80 -e PORT=8080 -e FAILURE_TEXT="Database connection failed. Please check your connection settings and try again." deploy-failure-page
```

### Markdown Formatted Message
```bash
docker run -d -p 8080:80 -e PORT=8080 -e FAILURE_TEXT="# Database Connection Error

## Issue Details
- **Error Code**: DB_CONN_001
- **Service**: Authentication Service
- **Port**: 8080

## Possible Causes
1. Database server is down
2. Invalid connection credentials
3. Network connectivity issues

## Resolution Steps
- Check database server status
- Verify connection string
- Contact database administrator

> **Note**: This is a critical system failure that requires immediate attention." deploy-failure-page
```

### Complex Multi-line Message
```bash
docker run -d -p 3000:80 -e PORT=3000 -e FAILURE_TEXT="Deployment Failed

Multiple issues detected:

1. Missing environment variables
2. Port conflicts detected
3. Resource limitations exceeded

Please review the deployment configuration and try again." deploy-failure-page
```

### Real-world PHP Error Example
```bash
docker run -d -p 8080:80 -e PORT=8080 -e FAILURE_TEXT="**Fatal Error Detected**

PHP Fatal error: Uncaught Dotenv\Exception\InvalidPathException: Unable to read environment file at [/var/www/html/public/../.env].

**Stack Trace:**
- /var/www/html/vendor/vlucas/phpdotenv/src/Store/FileStore.php:68
- /var/www/html/vendor/vlucas/phpdotenv/src/Dotenv.php:222
- /var/www/html/public/index.php:8

**Resolution:** Check if .env file exists and has proper permissions." deploy-failure-page
```

### Different Port Example
```bash
docker run -d -p 9090:80 -e PORT=9090 -e FAILURE_TEXT="Service failed on port 9090. Please check the logs." deploy-failure-page
```

## Environment Variables

- `FAILURE_TEXT`: The failure message to display. Supports both plain text and Markdown formatting. If not provided, defaults to "No failure details provided".
- `PORT`: The port number to display on the page. Should match the external port you're mapping to. If not provided, defaults to "80".

## Supported Markdown Features

The app automatically detects and renders the following Markdown syntax:

- **Headers**: `# H1`, `## H2`, `### H3`, etc.
- **Bold text**: `**bold text**`
- **Lists**: 
  - Bulleted: `- item` or `* item`
  - Numbered: `1. item`
- **Blockquotes**: `> important note`
- **Code**: `` `inline code` ``
- **Links**: `[text](url)`

## Container Management

### Stop Running Container
```bash
docker ps                    # Find container ID
docker stop [CONTAINER_ID]   # Stop the container
```

### Remove Container
```bash
docker rm [CONTAINER_ID]     # Remove stopped container
docker container prune -f    # Remove all stopped containers
```

### View Logs
```bash
docker logs [CONTAINER_ID]   # View container logs
```

## Build and Push to Docker Hub (Optional)

```bash
docker build -t hazelgallery/deploy-failure-page .
docker push hazelgallery/deploy-failure-page
```

## Troubleshooting

### Container Won't Start
- Check if port 8080 is already in use: `lsof -i :8080`
- Use a different port: `docker run -d -p 3000:80 ...`

### Markdown Not Rendering
- Ensure you're using the local image: `deploy-failure-page` (not `hazelgallery/deploy-failure-page`)
- Rebuild the image: `docker build -t deploy-failure-page .`
- Check that your text contains markdown syntax (`#`, `**`, etc.)

### Text Not Showing
- Verify the `FAILURE_TEXT` environment variable is set correctly
- Check container logs: `docker logs [CONTAINER_ID]`

### Browser Caching Issues
- Hard refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows/Linux)
- Open in incognito/private mode
- The app includes no-cache headers to prevent this issue

## Technical Details

- **Base Image**: nginx:alpine with Python3
- **Text Processing**: Python script handles environment variable substitution
- **Markdown Processing**: Client-side rendering using marked.js library
- **Styling**: Responsive CSS with error-themed design
- **Caching**: Disabled via meta tags to ensure fresh content
