docker build -t hostile-tweets .
docker tag hostile-tweets <docker-username>/hostile-tweets:v3
docker push <docker-username>/hostile-tweets:v3

oc new-app --name hostile-tweets --docker-image=docker.io/yeruham/hostile-tweets:v3
oc expose service/hostile-tweets
oc get route -l app=hostile-tweets