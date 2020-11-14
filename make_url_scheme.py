import shortcuts

def make_exec_url_scheme(install_path, unzipped_dirname, start_filename, argv=[]):
    if unzipped_dirname:
        start_path = install_path + '/' + unzipped_dirname + '/' + start_filename
        print(f"\nGenerating 'Exec' URL Scheme for: {start_path}")
        try:
            url_scheme = shortcuts.pythonista_url(path=start_path, action='exec', args="", argv=argv)
        except Exception as e:
            print(f"Make URL Scheme Err: {e}")
            url_scheme = None
        return url_scheme
    else:
        return None

def make_run_url_scheme(install_path, unzipped_dirname, start_filename, argv=[]):
    if unzipped_dirname:
        start_path = install_path + '/' + unzipped_dirname + '/' + start_filename
        print(f"\nGenerating 'Run' URL Scheme for: {start_path}")
        try:
            url_scheme = shortcuts.pythonista_url(path=start_path, action='run', args="", argv=argv)
        except Exception as e:
            print(f"Make URL Scheme Err: {e}")
            url_scheme = None
        return url_scheme
    else:
        return None
