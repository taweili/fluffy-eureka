extern crate core;

use quote::quote;
use proc_macro::TokenStream;
use syn::{parse_macro_input, DeriveInput, DataStruct, FieldsNamed};
use syn::Data::Struct;
use syn::Fields::Named;

#[proc_macro_attribute]
pub fn public(_attr: TokenStream, item: TokenStream) -> TokenStream {
    let ast = parse_macro_input!(item as DeriveInput);
    let name = ast.ident;


    /* --- version 1
    let public_version = quote! {
        pub struct #name {
            pub first: String, 
            pub second: String,
        }
    };
    */

    /* --- version 2 */
    let fields = match ast.data {
        Struct(
            DataStruct {
                fields: Named (
                    FieldsNamed {
                        ref named, ..
                    }
                ),
                ..
            }
        ) => named, 
        _ => unimplemented!("only works for structs with named fields")
    };

    let builder_fields = fields.iter().map(|f| {
        let name = &f.ident;
        let ty = &f.ty;
        quote! { pub #name: #ty}
    });

    let public_version = quote! {
        pub struct #name {
            #(#builder_fields),*
        }
    };

    public_version.into()
}
