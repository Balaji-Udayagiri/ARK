#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/core/core.hpp"
#include <iostream>
#include <math.h>

using namespace cv;

using namespace std;

int main() 
{
	struct size
	{
		int height;
		int width;
	}
	struct size kernel;
	kernel.height=5;
	kernel.width=5;
	int wsize=13;
	Mat imgleft = imread("left_image.jpg",0);
	GaussianBlur(imgleft, imgleft, 5, 0, 0, 1 );
	Mat imgright = imread("right_image.jpg",0);
	GaussianBlur(imgright, imgright, 5, 0, 0, 1 );	
	Mat Disparity(imgleft.rows,imgleft.cols,CV_8UC1,Scalar(0));
	for(int i=(wsize/2);i<imgleft.rows-(wsize/2);i++)
		for(int j=(wsize/2);j<imgleft.cols-(wsize)/2;j++)
		{
			long int minsum=1000000000;
			int reqval=-1;
			for(int k=(wsize/2);k<imgright.cols-(wsize/2);k++)
			{
				long int sum=0;			
				
				for(int l=-(wsize)/2;l<=(wsize)/2;l++)
					for(int m=(wsize)/2;m<=(wsize)/2;m++)
						sum+=(imgleft.at<uchar>(i-l,j-m)-imgright.at<uchar>(i-l,k-m))*(imgleft.at<uchar>(i-l,j-m)-imgright.at<uchar>(i-l,k-m));
				if(sum<minsum)
				{
					minsum=sum;
					reqval=k;
				}
				
			}
			int intensity=int (abs((255*(reqval-j)/(imgleft.cols-wsize+1))));
			Disparity.at<uchar>(i,j)=intensity;
	
  		}
  		namedWindow("win",1);
  		imshow("win",Disparity);
  		waitKey(0);
		
}