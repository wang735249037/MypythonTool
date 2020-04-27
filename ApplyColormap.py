
import cv2
import numpy as np

def ApplyColorMap(image,mn,mx,L=cv2.COLORMAP_RAINBOW,M=cv2.COLORMAP_RAINBOW,R=cv2.COLORMAP_RAINBOW):
	if len(image.shape)==3:
		image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	mask_1=cv2.inRange(image,mn,mx)
	maskd_Im=cv2.bitwise_and(image,image,mask=mask_1)
	maskd_Im = (maskd_Im-mn)*255.0/(mx-mn)
	maskd_Im = maskd_Im.astype(np.uint8)
	maskd_Im = cv2.applyColorMap(maskd_Im,M)
	if mn >0:
		mask_2=cv2.inRange(image,0,mn)
		resd_Im=cv2.bitwise_and(image,image,mask=mask_2)
		resd_Im = (resd_Im-0)*255.0/(mn)
		resd_Im = resd_Im.astype(np.uint8)
		resd_Im = cv2.applyColorMap(resd_Im,L)
		maskd_Im[np.where(mask_2 == 255)] = resd_Im[np.where(mask_2 == 255)]
	
	if mx <255:
		mask_3=cv2.inRange(image,mx,255)
		resd_Im=cv2.bitwise_and(image,image,mask=mask_3)
		resd_Im = (resd_Im-mx)*255.0/(255-mx)
		resd_Im = resd_Im.astype(np.uint8)
		resd_Im = cv2.applyColorMap(resd_Im,R)
		maskd_Im[np.where(mask_3 == 255)] = resd_Im[np.where(mask_3 == 255)]
	return maskd_Im
	
if __name__ == '__main__':
	I = cv2.imread(r'YourPath000000.bmp',0)
	res = ApplyColorMap(I,200,230)
	#res = ApplyColorMap(I,200,230,1,2,3)
	cv2.imshow('',res)
	cv2.waitKey(0)