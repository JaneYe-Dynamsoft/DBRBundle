Dynamsoft Barcode Reader SDK for Python
====================================================
|version| |python| |pypi| 

.. |version| image:: https://img.shields.io/pypi/v/dynamsoft_barcode_reader_bundle?color=orange
.. |python| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue
.. |pypi| image:: https://img.shields.io/pypi/dm/dynamsoft_barcode_reader_bundle


What You Should Know About Dynamsoft Barcode Reader
---------------------------------------------------
|trial|

.. |trial| image:: https://img.shields.io/badge/Get-30--day%20FREE%20Trial-blue
            :target: https://www.dynamsoft.com/customer/license/trialLicense/?product=dbr&package=python

`Dynamsoft Barcode Reader SDK <https://www.dynamsoft.com/barcode-reader/overview/?utm_source=pypi>`_ 
enables you to efficiently embed barcode reading functionality in your
web, desktop or mobile application using just a few lines of code.
Saving you months of added development time and resources, our SDK can
create high-speed and reliable barcode scanner software applications to
meet your business needs.

About Python Barcode SDK
-------------------------
The Python Barcode SDK is a wrapper for Dynamsoft C++ Barcode SDK. It comes with all the general
features of Dynamsoft Barcode Reader, bringing convenience for Python developers.


Notice: Package Renamed and Updated
-----------------------------------
`dynamsoft_barcode_reader_bundle` is the successor to the `dbr` package, starting from version 10.
This new version introduces significant architectural improvements and a redesigned API to integrate with
`DynamsoftCaptureVision (DCV) <https://www.dynamsoft.com/capture-vision/docs/core/introduction/index.html?lang=python>`_ architecture,
which is newly established to aggregate the features of functional products powered by Dynamsoft.


Version
-------

-  11.0.1000

Supported Platforms
-------------------

- Windows x64

- Linux(x64, ARM64)

- macOS (10.15+)

Supported Python Versions
-------------------------
-  Python3.13

-  Python3.12

-  Python3.11

-  Python3.10

-  Python3.9

-  Python3.8

Installation
------------

   pip install dynamsoft_barcode_reader_bundle

Supported Symbologies
---------------------

-  Linear Barcodes (1D) :

   -  Code 39 *(including Code 39 Extended)*
   -  Code 93
   -  Code 128
   -  Codabar
   -  Interleaved 2 of 5
   -  EAN-8
   -  EAN-13
   -  UPC-A
   -  UPC-E
   -  Industrial 2 of 5
   -  MSI Code
   -  Code 11

-  2D Barcodes :

   -  QR Code *(including Micro QR Code)*
   -  Data Matrix
   -  PDF417 *(including Micro PDF417)*
   -  Aztec Code
   -  MaxiCode *(mode 2-5)*
   -  DotCode

-  Patch Code

-  Pharmacode

-  GS1 Composite Code

-  GS1 DataBar :

   -  Omnidirectional
   -  Truncated
   -  Stacked
   -  Stacked Omnidirectional
   -  Limited
   -  Expanded
   -  Expanded Stacked

-  Postal Codes :

   -  USPS Intelligent Mail
   -  Postnet
   -  Planet
   -  Australian Post
   -  UK Royal Mail

Quick Start
-----------
.. code-block:: python

   from dynamsoft_barcode_reader_bundle import *

   # Apply for a trial license: https://www.dynamsoft.com/customer/license/trialLicense/?product=dbr&utm_source=pypi
   license_key = "Input your own license"
   image = r"Please input your own image path"
   LicenseManager.init_license(license_key)
   cvr = CaptureVisionRouter()

   try:
      
     capturedResult = cvr.capture(image,EnumPresetTemplate.PT_READ_BARCODES.value)

     items = capturedResult.get_items()

     for i in range(len(items)):
        barcode = items[i]
        print("Barcode Format : ")
        print(barcode.get_format_string())
        print("Barcode Text : ")
        print(barcode.get_text())             
        print("-------------")
   except Exception as e:
     print(e)


Sample Code
------------
https://github.com/Dynamsoft/barcode-reader-python-samples

Documentation
-----------------

- `API <https://www.dynamsoft.com/barcode-reader/docs/server/programming/python/api-reference/?utm_source=pypi>`_
- `User Guide <https://www.dynamsoft.com/barcode-reader/docs/server/programming/python/user-guide.html?utm_source=pypi>`_
- `Release Notes <https://www.dynamsoft.com/barcode-reader/docs/server/programming/python/release-notes/python-10.html?utm_source=pypi>`_


Contact Us
----------

support@dynamsoft.com
