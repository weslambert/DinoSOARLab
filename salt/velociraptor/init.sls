{%- set url_base = salt['pillar.get']('global:url_base') %}
velociraptorgroup:
  group.present:
    - name: velociraptor
    - gid: 989

velociraptor:
  user.present:
    - uid: 989
    - gid: 989
    - home: /opt/so/conf/velociraptor

#velociraptorconfdir:
#  file.directory:
#    - name: /opt/so/conf/velociraptor
#    - user: 939
#    - group: 939
#    - makedirs: True

so-velociraptor:
  docker_container.running:
    - image: wlambert/so-velociraptor
    - binds:
      - /opt/so/conf/velociraptor:/velociraptor:rw
    - port_bindings:
      - 0.0.0.0:8889:8889
      - 0.0.0.0:8001:8001
      - 0.0.0.0:8000:8000
    - environment:
      - VELOX_SERVER_URL=https://{{ url_base }}:8000/
      - VELOX_FRONTEND_HOSTNAME={{ url_base }}
