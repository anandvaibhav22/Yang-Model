pipeline{
 agent any
    Stages{
       stage("build"){
             steps{
             sh 'npm install'
             sh 'npm build'
          }
    }
    stage("test"){
             steps{
             		echo 'Test stage'
                  }
        }

    stage("deploy"){
             steps{
             	echo 'Deploy'
           }
    }

    }

}
