-----------------build and run 1st container----------------
cd p1
docker build -t loop-container .
docker run loop-container

-----------------build and run 2nd container----------------
cd p2
docker build -t sort-container .
docker run sort-container

-----------------build and run 3rd container----------------
cd p3
docker build -t nestloop-container .
docker run nestloop-container

-----------------push image to docker hub----------------
docker tag loop-container binbinweng/loop:v1
docker push binbinweng/loop:v1

docker tag sort-container binbinweng/sort:v1
docker push binbinweng/sort:v1

docker tag nestloop-container binbinweng/nestloop:v1
docker push binbinweng/nestloop:v1

-----------------build the workflow with argo workflow --------
- the three yml files are for creating the workflow for three 
- types of DAG applications including a normal DAG, a FFT DAG,
- and a GE DAG.
