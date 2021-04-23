pip install virtualenv
virtualenv CEnv
CEnv\Scripts\activate
pip install -r requirements.txt
cd PyAutoMail
python Passwords/Save_Password.py (Write your password here)
cd .. (Go up one directory)
python PyAutoMail/AutoMailer.py
python PyAutoMail/AutoReplacer.py
