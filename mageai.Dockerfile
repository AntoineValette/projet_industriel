FROM mageai/mageai:latest

EXPOSE 6789

ENTRYPOINT ["/app/run_app.sh", "mage", "start", "smartETL"]