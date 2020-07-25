use actix_web::{HttpResponse};
use serde::{Deserialize, Serialize};
use rand::{thread_rng, Rng};
use rand::distributions::Alphanumeric;

#[derive(Serialize, Deserialize)]
struct ResponseObj {
    result: String,
}


async fn mainapi() -> HttpResponse {
    let rand_string: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .take(30)
        .collect();
    HttpResponse::Ok().json(ResponseObj {
        result: rand_string,
    })
}


#[actix_rt::main]
async fn main() -> std::io::Result<()> {
    use actix_web::{web, App, HttpServer};

    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(mainapi))
    })
    .bind("0.0.0.0:8088")?
    .run()
    .await
}
