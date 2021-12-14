# REST BASED BLOCKCHAIN

**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the application and API**

Make sure to activate the virtual environment.

**Run a peer instances**
```
python3 -m backend.app
export PEER=True && python3 -m backend.app
```

**How to use**
```
We can do python3 -m backend.scripts.test_app to test the blockchain via script
```

**Or we can use the frontend**
```
cd frontend
npm install
npm run start
```

