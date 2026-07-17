#[derive(Debug, Clone)]
struct Tensor {
    data: Vec<f32>,
    shape: Vec<usize>,
}

impl Tensor {
    fn new(data: Vec<f32>, shape: Vec<usize>) -> Tensor {
        Tensor { data, shape }
    }

    fn zeros(shape: Vec<usize>) -> Tensor {
        // TODO: create a Tensor filled with 0.0, with the given shape
        let total: usize = shape.iter().product();
        let data = vec![0.0, total]
    }
}

fn main() {
    let t = Tensor::new(vec![1.0, 2.0, 3.0, 4.0], vec![2, 2]);
    println!("{:?}", t);
}