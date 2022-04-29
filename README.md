### Radar Scope
## A weather radar application written in Python

## To use this software:
1. Clone the repository onto your computer using `git clone --recurse-submodules https://github.com/shulltronics/radar-scope.git`
2. Create a python virtual environment with `python -m venv .venv`
3. Activate the virtual environment with `source .venv/bin/activate` (assuming you are using bash on Linux)
4. Install the dependencies for unigui with `cd displayio-universal-ui` followed by `pip install -r requirements.txt`
5. Install the dependencies for radar-scope with `pip install -r requirements.txt` from the root of the repository
   TODO: why don't the nested submodules from `displayio-universal-ui` get installed if I skip step 4 and just run step 5? It seems like the upstream adafruit_blinka library is installed rather than the submodule.