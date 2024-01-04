use ollama_rs::{
    generation::completion::{
        request::GenerationRequest,
    },
    Ollama,
};

#[tokio::main]
async fn main() {
    let ollama = Ollama::default();
    let model = "mistral".to_string();
    let prompt = "why is sky blue?".to_string();

    let res = ollama.generate(GenerationRequest::new(model, prompt)).await;

    if let Ok(res) = res {
        println!("{}", res.response);
    }
}
