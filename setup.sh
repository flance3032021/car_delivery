mkdir -p ~/.streamlit/
echo "[general]
email = \"flance3032021@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml