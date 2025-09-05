#!/usr/bin/env python3
import os

# get environment variables
failureText = os.environ.get('FAILURE_TEXT', 'No failure details provided')
port = os.environ.get('PORT', '80')

# read template file
with open('/tmp/index.html', 'r') as f:
    content = f.read()

# replace placeholders with actual values
content = content.replace('${FAILURE_TEXT}', failureText)
content = content.replace('${PORT}', port)

# write processed file
with open('/usr/share/nginx/html/index.html', 'w') as f:
    f.write(content)
