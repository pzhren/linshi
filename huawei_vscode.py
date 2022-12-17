commit_id=f06011ac164ae4dc8e753a3fe7f9549844d15e35
vscode_dir=~/.vscode-server/bin/${commit_id}

# Download url is: https://update.code.visualstudio.com/commit:${commit_id}/server-linux-x64/stable
curl -sSL "https://update.code.visualstudio.com/commit:${commit_id}/server-linux-x64/stable" -o vscode-server-linux-x64.tar.gz

mkdir -p $vscode_dir
# assume that you upload vscode-server-linux-x64.tar.gz to /tmp dir
tar zxvf /tmp/vscode-server-linux-x64.tar.gz -C $vscode_dir --strip 1
touch $vscode_dir/0