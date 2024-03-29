ARG branch=latest
FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH extractor.Dequarantine

USER assemblyline

WORKDIR /opt/al_service
COPY . .

ARG version=4.2.0.dev1
RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml
