#!/usr/bin/env python3
###Vorlage: The Morpheus Tutorials "https://github.com/TheMorpheus407/Python-Lets-Code"

import datetime
import psutil
from tabulate import tabulate
import os
import time

def get_processes():
    procs = []
    for p in psutil.process_iter():
        with p.oneshot():
            pid = p.pid
            if pid == 0:
                continue
            name = p.name()
            try:
                create_time = datetime.datetime.fromtimestamp(p.create_time())
            except OSError:
                create_time = datetime.datetime.fromtimestamp(psutil.boot_time())
            cpu_usage = p.cpu_percent()
            try:
                cpu_affinity = len(p.cpu_affinity())
            except psutil.AccessDenied:
                cpu_affinity = "Berechtigung Verweigert!"
            status = p.status()
            try:
                memory = p.memory_full_info().uss
            except psutil.AccessDenied:
                memory = "Berechtigung verweigert!"
            try:
                user = p.username()
            except psutil.AccessDenied:
                user = "Berechtigung verweigert!"
            try:
                nice = p.nice()
            except psutil.AccessDenied:
                nice = "Berechtigung verweigert!"
        procs.append({
            'PID': pid,
            'Name': name,
            'Erstellungszeit': create_time,
            'CPU Auslastung': cpu_usage,
            'Erlaubte CPU-Kerne': cpu_affinity,
            'Status': status,
            'Arbeitsspeicher Auslastung': memory,
            'Benutzer': user,
            'Wichtigkeit': nice
        })
    return procs


def print_processes(ps):
    print(tabulate(ps, headers="keys", tablefmt='github'))

procs = get_processes()
while True:
    print_processes(procs)
    time.sleep(5)
    procs = get_processes()
    if "nt" in os.name:
        os.system("cls")
    else:
        os.system("clear")
