
#docker build -t mec-mini-projects .

#sudo docker run --network host --mount type=bind,source="$(pwd)"/mec-mini-projects,target=/app mec-mini-projects jupyter notebook --allow-root --ip 0.0.0.0

#docker run -p 8888:8888 --mount type=bind,source="$(pwd)"/mec-mini-projects,target=/app mec-mini-projects jupyter notebook --allow-root --ip 0.0.0.0
