RESULTS=$(git log -1 --pretty=%B | grep 'GREEN')
echo "$RESULTS"