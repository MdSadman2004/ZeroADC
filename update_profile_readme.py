import urllib.request, json, base64, os

token = open(os.path.expanduser('~/.github/token')).read().strip()
owner = 'MdSadman20040812'
repo = 'MdSadman20040812.github.io'
path = 'README.md'

url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
req = urllib.request.Request(url, headers={
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json',
    'User-Agent': 'HermesAgent'
})
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read())

content = base64.b64decode(data['content']).decode('utf-8', errors='replace')
print('Current length:', len(content))
print('SHA:', data['sha'])

append_block = (
    "| **[AgentForge](https://github.com/MdSadman20040812/AgentForge)** "
    "| Falsification-first agentic automation framework with hash-based change detection and parallel subagent refinement "
    "| Python, Automation, Validation |\n"
    "| **[ZeroADC](https://github.com/MdSadman20040812/ZeroADC)** "
    "| Zero-ADC analog front-end with CDM fusion for batteryless event-driven nodes; validated across simulation, Renode M33, and Arduino UNO "
    "| Embedded, Python, Arduino, Renode |\n"
)

marker = '## Tech Stack'
if marker in content:
    content = content.replace(marker, append_block + marker)
else:
    content += '\n' + append_block

print('New length:', len(content))
print('---END PREVIEW---')
print(content[-900:])
print('---END---')

encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')
payload = json.dumps({
    'message': 'docs: add AgentForge and ZeroADC to featured projects',
    'content': encoded,
    'sha': data['sha']
}).encode('utf-8')

put_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
put_req = urllib.request.Request(put_url, data=payload, headers={
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json',
    'Content-Type': 'application/json',
    'User-Agent': 'HermesAgent'
}, method='PUT')
with urllib.request.urlopen(put_req, timeout=15) as r:
    result = json.loads(r.read())
print('Commit SHA:', result.get('commit', {}).get('sha'))
print('Updated:', result.get('content', {}).get('html_url'))
