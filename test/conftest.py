import os
import shutil, tempfile

os.environ['prometheus_multiproc_dir'] = tempfile.mkdtemp()

def pytest_configure(config):
  if not os.path.exists(os.environ['prometheus_multiproc_dir']):
      os.makedirs(os.environ['prometheus_multiproc_dir'])
  return config

def pytest_unconfigure(config):
  shutil.rmtree(os.environ['prometheus_multiproc_dir'])
  return config