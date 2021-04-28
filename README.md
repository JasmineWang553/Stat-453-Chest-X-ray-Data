# Stat-453-Chest-X-ray-Data

### COVID and Lung Disease Detection from Xray images
- **Intro**: Failure to detect lung disorders or have delayed diagnosis brings devastating results for the patient. Due to the quick spread of COVID-19, many patients were unable to access required treatments in time. Therefore, in order to address these issues, we are motivated to develop deep learning models that can quickly and accurately classify lung diseases and address them with the corresponding treatments in a timely matter.
- **Goal**: Train models on detecting Covid-19, Viral Pneumonia, heathy lungs and Lung Opacity from X-ray images using transfer learning on Convolutional Neural Networks (CNN): DenseNet, ResNet, AlexNet, and a benchmark model with Logistic Regression.
- **Tech used**: Pytorch, pandas, numpy, opencv<br>

## Dataset
- [link to dataset](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database)
- M.E.H. Chowdhury, T. Rahman, A. Khandakar, R. Mazhar, M.A. Kadir, Z.B. Mahbub, K.R. Islam, M.S. Khan, A. Iqbal, N. Al-Emadi, M.B.I. Reaz, M. T. Islam, “Can AI help in screening Viral and COVID-19 pneumonia?” IEEE Access, Vol. 8, 2020, pp. 132665 - 132676. [Paper link](https://ieeexplore.ieee.org/document/9144185)
- Rahman, T., Khandakar, A., Qiblawey, Y., Tahir, A., Kiranyaz, S., Kashem, S.B.A., Islam, M.T., Maadeed, S.A., Zughaier, S.M., Khan, M.S. and Chowdhury, M.E., 2020. Exploring the Effect of Image Enhancement Techniques on COVID-19 Detection using Chest X-ray Images. [Paper Link](https://www.sciencedirect.com/science/article/pii/S001048252100113X?via%3Dihub)

## Files
- jupyter notebooks:
  1. Logistic Regression 
  2. AlexNet 
  3. VGG19 with batch norm
  4. ResNet50

- helper_functions: dataset, evaluation, train, plotting are written by Professor [Sebastian Raschka](https://github.com/rasbt/stat453-deep-learning-ss21/tree/main/L13/code)
- helper_GradCAM: code borrowed from Kaggle Notebook by [Debarshi Chanda](https://www.kaggle.com/debarshichanda/gradcam-visualize-your-cnn) 
