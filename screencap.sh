if [[ -n $1 ]]; then
	adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $1.png
else
    echo "argument error"
    echo "please use with imagename.png"
	exit 1
fi
