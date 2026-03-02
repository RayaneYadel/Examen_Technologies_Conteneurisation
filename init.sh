# créer le venv si absent
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# activer le venv
# - Windows (Git Bash) : .venv/Scripts/activate
# - Linux/macOS        : .venv/bin/activate
if [ -f ".venv/Scripts/activate" ]; then
  source .venv/Scripts/activate
else
  source .venv/bin/activate
fi


# deps
python3 -m pip install -r requirements.txt

python3 -m pip install -U ipykernel
python3 -m ipykernel install --user --name venv --display-name "venv"

echo "OK: env .venv'"
