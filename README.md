# EyeQCheck

EyeQCheck is an early Django prototype exploring how a camera can detect a printed reference square and use its apparent size to estimate the viewer's distance. The app records that estimate in SQLite and uses it to scale an eye-chart image in the browser.

## What this project demonstrates

- A Django app with server-rendered pages, forms, and a SQLite-backed model.
- Using OpenCV and NumPy to capture a webcam frame and process it to find a square.
- Passing a calculated value from a Django view to a template to scale an image.

The repository contains the implementation of this flow; it does not establish clinical accuracy or provide a medical diagnosis. This is a prototype, not a validated vision test or production-ready service.

## Stack

- Python and Django 4.1.7
- OpenCV and NumPy
- SQLite

## Prerequisites

- Python 3, with `venv` and `pip` available.
- A webcam accessible as camera index 0 from the machine running Django.
- A printed copy of [`referenceSquare.pdf`](referenceSquare.pdf), which the app uses as its size reference.

## Run locally

From the repository root:

```sh
cd django
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. Place the printed square within the camera's view, then select **Take Photo!**. The app uses the webcam connected to the machine running Django. The initial migration is already checked in, so `migrate` applies it; there is no need to run `makemigrations`.

If creating the virtual environment fails because the OS does not have its Python `venv` support installed, install the matching system package using your operating system's package manager, then retry. No `sudo` is needed for the project setup itself.

## Tests

From `django/`, with the virtual environment active:

```sh
python manage.py test
```

The repository currently contains only Django's generated placeholder test file; no project-specific automated tests are implemented yet.

## Status and limitations

This repository is an early prototype. Its Django settings enable development mode, and its webcam capture and image-processing flow has not been validated as a medical or clinical measurement. No deployed demo or production configuration is provided.
