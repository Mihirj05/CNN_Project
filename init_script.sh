echo " A script to create, activate and install requirements.txt"
echo "....."

virtualenv venu

echo "creation of virtualenv done...."
echo "Activation my env"

source venv/bin/activate

echo "......"
echo "Install requirements.txt"

pip install -r requirements.txt

sleep(2)
echo "install done"
echo "Creation activation and install done"