pipeline{
 agent any
    stages{
       stage("build"){
             steps{
                echo 'build stage'
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
              sh 'hello.py'
           }
    }

    }

}
