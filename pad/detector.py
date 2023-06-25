import torch
import torchvision.models as models
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

class PAD():
	def __init__(self, modelPath) -> None:
		self.device = torch.device("cpu")
		self.weights = torch.load(modelPath, map_location=self.device)
		self.DNetPAD = models.densenet121(pretrained=True)
		self.num_ftrs = self.DNetPAD.classifier.in_features
		self.DNetPAD.classifier = nn.Linear(self.num_ftrs, 2)
		self.DNetPAD.load_state_dict(self.weights['state_dict'])
		self.DNetPAD = self.DNetPAD.to(self.device)
		self.DNetPAD.eval()
		self.transform = transforms.Compose([
							transforms.Resize([224, 224]),
							transforms.ToTensor(),
							transforms.Normalize(mean=[0.485], std=[0.229])])

	def get_pad_score_from_image(self, image):
		tranformImage = self.transform(image)
		tranformImage = tranformImage.repeat(3, 1, 1)
		tranformImage = tranformImage[0:3,:,:].unsqueeze(0)
		tranformImage = tranformImage.to(self.device)
		output = self.DNetPAD(tranformImage)
		PAScore = output.detach().cpu().numpy()[:, 1]
		PAScore = np.minimum(np.maximum((PAScore+15)/35,0),1)
		return PAScore[0]

	def get_pad_score(self, image_path):
		image = Image.open(image_path)
		tranformImage = self.transform(image)
		image.close()
		tranformImage = tranformImage.repeat(3, 1, 1)
		tranformImage = tranformImage[0:3,:,:].unsqueeze(0)
		tranformImage = tranformImage.to(self.device)
		output = self.DNetPAD(tranformImage)
		PAScore = output.detach().cpu().numpy()[:, 1]
		PAScore = np.minimum(np.maximum((PAScore+15)/35,0),1)
		return PAScore[0]






