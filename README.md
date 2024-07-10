This is a simple service API for current currency conversion

Parameters:

- 'from': Currency to convert from
- 'to': Currency to convert to

An Example request would look like:

GET /convert?from=EUR&to=USD

With a return looking like:

{
"rate": 1.08140186
}


To deploy this please use the following steps:

Build the Docker image

kubectl apply -f k8s/deployment.yaml

kubectl apply -f k8s/service.yaml


This is all that is needed to build this


You can test via:

curl "http://localhost:30000/convert?from=XXX&to=YYY"

Replace XXX and YYY with desired currencies

