package main
import (
   "fmt"
)

func sumVector(v1 []int, v2 []int) []int{
   result := []int{}
   
   for i := 0; i < len(v1); i++ {
      result = append(result, v1[i]+v2[i])
   }
   
   return (result)
}

func subVector(v1 []int, v2 []int) []int{
   result := []int{}

   for i := 0; i < len(v1); i++ {
      result = append(result, v1[i]-v2[i])
   }

   return (result)
}

func main() {

   vec1 := []int{1, 2, 3}
   vec2 := []int{4, 2, 5}

   // Testing
   sum := sumVector(vec1, vec2)
   sub := subVector(vec1, vec2)
   fmt.Println(sum, "and" ,sub)

}

