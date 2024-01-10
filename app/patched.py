def get_patched_app():
    from gevent import monkey
    from psycogreen.gevent import patch_psycopg

    monkey.patch_all()  # gevent patch to support implicit asynchronous
    patch_psycopg()  # patch psycopg2 to support implicit asynchronous

    from app.main import app

    return app


app = get_patched_app()
