# Image-recognition
This project is aim to use rasperry pi camera to classify image.
Current goal is to identify number from 0 - 9. The project aims
to allow author to have basic knowledge to develop next project,
which uses rasperry pi to do real time sitting and standing posture
analysis and alert the user of bad posture.

## Device
rasperry pi 5
## Milestone
1. generate 28x28 image of 0 - 9 grayscale image. Classify image with CNN tensorflow lite
2. deploy tensorflow lite in rpi. Use it to classify generated
image of 0 - 9 (grayscale and rgb)
3. use pi camera to capture written 0 - 9. Convert to grayscale
with opencv. Classify with tensorflow lite. Then attempt rgb.

## Dependency
The python depedency satsifies both this current project and also
should give least modification to posture project.
