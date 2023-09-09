# Kitchen Utensils Image Classification Project

This project focuses on building a kitchen utensils image classification system using Convolutional Neural Networks (CNNs). 
The goal is to classify images of various kitchen utensils into predefined categories. The project is containerized with Docker 
and managed with Kubernetes (K8s) for scalability and easy deployment.

Table of Contents 
Introduction
Project Structure
Prerequisites

Introduction
Kitchen utensils image classification is a common problem in computer vision. This project demonstrates how to create, train, 
and deploy a CNN model to classify images of kitchen utensils, such as knives, forks, spoons, and spatulas. The model is capable 
of distinguishing between different utensil categories with high accuracy.

Project Structure
The project structure is organized as follows:
data/: Contains training and testing datasets. 
models/: Stores pre-trained models and model checkpoints. 
docker/: Docker configuration files for containerization. 
kube-config/: Kubernetes yaml files for deployment and scaling.

Prerequisites 
Python 3.7+ 
TensorFlow 
Docker (for containerization) 
Kubernetes (for cluster deployment and management)
