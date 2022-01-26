Authors:
- Kajetan Kubik
- Bartosz Maślanka

Important Colabs Notebooks:
- [Style Transfer](https://colab.research.google.com/drive/1eSayvcQOY80RUIGCsGpD0pVxwtMF7KOH?usp=sharing)
- [Model Blending](https://colab.research.google.com/drive/1ae7LhhPscu4AKqgXY3c9P69urqmLIlLj?usp=sharing)

# Style Transfer

Family of AI algorithms that refers to manipulating images. In short, the main goal is to transfer the style of one image into another. My favorite website to do this is [DeepDream](https://deepdreamgenerator.com/). 
 
Traditional methods rely on manipulating image in such a way that
the sum of losses(differences) between: (target image, original image) and (target image, style image) was the lowest. To do this most often pretrained VGG19 (Neural Network model) is used, along with mathematical tools like Gram matrix.

<p float="left">
  <img src="https://drive.google.com/uc?export=download&id=1MT_UeiDna57hj5Hq4_4n6voOswjaduAg" width="190" />
  <img src="https://cdn2.iconfinder.com/data/icons/ios-7-icons/50/plus-512.png" width="190" />
  <img src="https://drive.google.com/uc?export=download&id=1LET5bPP95ZZ3dxY1A2Ud1b8fnK_SAYhz" width="230" /> 
  <img src="https://pngimg.com/uploads/equals/equals_PNG35.png" width="190" /> 
  <img src="https://drive.google.com/uc?export=download&id=1GEMPlpS2XXAjLhmR1CIMz9wkr2y7RTMO" width="190" /> 
</p>

# Style Transfer 2.0

In december 2018 Nvidia introduced a GAN network called StyleGAN.
Here I work on StyleGAN2, however recently even StyleGAN3 was published.

This model allows us to change image content in control mode. Most popular way is to change the characteristics of humans in pictures (things like age or smile). [Good example.](https://github.com/woctezuma/stylegan2-projecting-images)

In the same manner we can change the style of the image. We just need pretrain StyleGAN, which can generate human faces, and pretrain StyleGAN, which can generate Style.

# StyleGAN

StyleGAN is a type of GAN. Article titled "A Style-Based Generator Architecture for Generative Adversarial Networks" was published by Nvidia in 2018. 

The paper proposes a new generator architecture for GAN that allows the control of different levels of detail in the generated samples from coarse details (e.g. head shape) to fine details (e.g. eye color).

One of the main ideas that distinguished this architecture among others was Progressive GAN. At the beginning the network is trained in low resolution (4x4), and next layers are added after getting satisfying results. Thanks to this, the training process is much more stable.

![](https://drive.google.com/uc?export=download&id=1x8ND9z74SUWk0Oob1DHolbEhHKSCnyo1)

  *Progressive Growing GAN [Source: Sarah Wolf]*
 
Another thing is replacing traditional common latent code for each layer (W(1,\*)) with separate latnet code for each layer (W(18,\*)).


The possibilities of this model are incredible. Take for example StyleGan that generates art images. GAN (in general) was created to create new, in this case, art images. For each input ( vector of 18 x 512 ) random values it returns a new art. It means that for one input, output will always be the same. So what if we could control this input? If we, theoretically, transforme our image into this latent code, could we change ourselves into art? YES. We have to do a little trick: we have to try ‘quess’ latent code that would produce us (or more precisely: image similar to us) on a model that created Humans. That's it. We then can feed this code to models that create art. This is the effect. 

![](https://drive.google.com/uc?export=download&id=1Ot9y_ni387Ru1jdyJtzoe0YrnZWVo2pK)

What is more, we can freely manipulate this latent code. We can change our hair style, facial expression, age or even sex. 

![](https://drive.google.com/uc?export=download&id=1_thLWfTxRs5BbTQ8OzhblsQ4oq4rCPDH)

But can we change our species? First, we have to create one.

# Blending Models

How is this process going? First we need to have two models that have the same config and same resolution. We copy weights from the first one, and after some chosen upscaling layer, we copy values from another.

![](https://drive.google.com/uc?export=download&id=1uq-bC9rN62l48tBUrlwdvP7M0O2h-N0O)

Why bother? Beacuse if image does not reminds face, our method is useless.

# Examples of Blended Models


<p float="left">
  <img src="reports/figures/blended-earth-people-64.jpg" alt="drawing" width="384"/>
  <img src="reports/figures/anime-256.jpg" alt="drawing" width="384"/>
  <img src="reports/figures/blended-faces-draw-32.jpg" alt="drawing" width="384"/>
  <img src="reports/figures/blended-faces-texture-8.jpg" alt="drawing" width="384"/>
</p>

# Examples of Style Transfers

# Used tools

- MlFlow
- Tensorboard
- Docker


# Links

https://github.com/justinpinkney/awesome-pretrained-stylegan2

https://towardsdatascience.com/style-transfer-with-gans-on-hd-images-88e8efcf3716

https://github.com/maciej3031/comixify

https://www.kaggle.com/momincks/paintings-for-artistic-style-transfer?select=Edvard+Munch+-+The+Scream.jpg

https://github.com/akanimax/msg-stylegan-tf

<!-- https://github.com/justinpinkney/toonify/blob/master/toonify-yourself.ipynb -->

https://github.com/matthias-wright/flaxmodels

https://github.com/matthias-wright/flaxmodels/blob/main/flaxmodels/stylegan2/stylegan2_demo.ipynb

<!-- https://github.com/justinpinkney/toonify/blob/master/StyleGAN-blending-example.ipynb -->

https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123670171.pdf

https://openaccess.thecvf.com/content_ICCV_2019/papers/Abdal_Image2StyleGAN_How_to_Embed_Images_Into_the_StyleGAN_Latent_Space_ICCV_2019_paper.pdf

https://medium.com/swlh/hairstyle-transfer-semantic-editing-gan-latent-code-b3a6ccf91e82

https://github.com/woctezuma/stylegan2-projecting-images


