import os
import glob
import logging
import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from collections import deque
import time

# Configure logging
logger = logging.getLogger(__name__)

# Proxy list
PROXIES = [
    {"ip": "38.153.152.244", "port": "9594", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "86.38.234.176", "port": "6630", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "173.211.0.148", "port": "6641", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "161.123.152.115", "port": "6360", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "216.10.27.159", "port": "6837", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "154.36.110.199", "port": "6853", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "45.151.162.198", "port": "6600", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "185.199.229.156", "port": "7492", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "185.199.228.220", "port": "7300", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
    {"ip": "185.199.231.45", "port": "8382", "username": "tfkzunmh", "password": "c0cwpmv652l8"},
]

def get_random_proxy():
    