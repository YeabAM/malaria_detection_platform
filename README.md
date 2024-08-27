# Malaria Detection System

This project is a deep learning-based malaria detection system that uses Convolutional Neural Networks (CNN) to detect the presence of malaria in blood smear images. In addition to detecting whether malaria is present, the system also identifies the type of Plasmodium strain responsible for the infection.

## Overview

Malaria is a life-threatening disease caused by parasites that are transmitted to humans through the bites of infected mosquitoes. Early and accurate diagnosis is critical for effective treatment. This system automates the detection of malaria from blood smear images, providing a fast, reliable, and scalable solution. The system not only identifies the presence of malaria but also classifies the specific Plasmodium strain (e.g., _P. falciparum_, _P. vivax_, etc.), assisting in the selection of appropriate treatment.

## Technology

- **TensorFlow:** Used for building and training the Convolutional Neural Network (CNN) model that detects and classifies malaria from blood smear images.
- **OpenCV:** Utilized for image processing tasks such as loading, resizing, and augmenting blood smear images to improve model accuracy.
- **Pandas:** Employed for data manipulation and analysis within the machine learning pipeline.
- **Django:** Provides the backend framework for building the business logic, managing model deployment, and handling user interactions via a web interface.
