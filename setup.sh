pip3 install -r requirements.txt
mkdir $HOME/.sashin
mv * $HOME/.sashin
printf "python3 $HOME/.sashin/main.py" > $PREFIX/bin/sashin
chmod +x $PREFIX/bin/sashin
printf "Install successfuly, run 'sashin' to continue"
rm -rf ../SashinKakushi