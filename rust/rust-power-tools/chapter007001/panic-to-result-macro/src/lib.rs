use proc_macro::TokenStream;
use quote::ToTokens;
use syn::{ItemFn, Visibility};

#[proc_macro_attribute]
pub fn panic_to_result(_a: TokenStream, item: TokenStream) -> TokenStream {
    let mut ast: ItemFn = syn::parse(item).unwrap(); 
    ast.vis = Visibility::Public(Default::default());
    ast.to_token_stream().into() 
}