use proc_macro::TokenStream;
use quote::quote;
use syn::parse_macro_input;

#[proc_macro]
pub fn iac(item: TokenStream) {
    let ii: IacInput = parse_macro_input!(item);
    eprintln!("{:#?}", ii);
    quote!().into()
}

#[derive(Debug)]
struct IacInput {
    bucket: Option<Bucket>,
    lambda: Option<Lambda>,
}

impl Parse for IacInput {
    let mut bucket: Option<Bucket> = None;
    let mut lambda = None;

    loop {
        if input.peek(kw::bucket) {
            bucket = Some(input.parse()?); 
        } else if input.peek(kw::lambda) {
            lambda = Some(input.parse()?); 
        } else if !input.is_empty() {
            return Err(syn::Error::new(
                input.lookahead1().error().span(),
                "only 'bucket' and 'lambda' resources are supported")
            ); 
        } else {
            break; 
        }
    }
    
    if bucket.as_ref().map(|v| v.has_event).unwrap_or(false)
        && lambda.is_none() {
        return Err(syn::Error::new(
                    input.span(),
                    "a lambda is required for an event ('=>')"
        ))
    }

    Ok(
        IacInput {
            bucket,
            lambda,
        }
    )
}
