#docker run --name alertmanager -d -p 127.0.0.1:9093:9093 quay.io/prometheus/alertmanager

docker run --name alertmanager -d -p 127.0.0.1:9093:9093 \
  -v /Users/ajaysingh/ws/master-python/programing_interview/go/go-prometheus/alertmanager.yml:/etc/alertmanager/alertmanager.yml \
  quay.io/prometheus/alertmanager