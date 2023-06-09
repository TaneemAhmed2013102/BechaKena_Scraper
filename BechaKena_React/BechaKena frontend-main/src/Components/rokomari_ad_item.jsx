import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTag } from "@fortawesome/free-solid-svg-icons";

function AdItemRokomari(props) {
   console.log(props);
  return (
    <>  
        <div className="card mb-3">
        <div className="row g-0">
          <div className="col-4 border-end border-2">
            <div className="d-flex justify-content-center">
            <img src={props.ad.image_path}
                className="img-fluid rounded-start"
                alt="..."
                style={{ maxHeight: "180px" }}
              />
            </div>
          </div>
          <div className="col-8">
            <div className="card-body pb-1">
              <h3 className="card-title text-dark">{props.ad.title}</h3>
              <div className="d-flex">
                <p className="card-text">
                  <small className="text-muted">
                    <FontAwesomeIcon icon={faTag} /> {props.ad.author}
                  </small>
                </p>
              </div>
              <p className="card-text text-success fw-bold">
                Tk {props.ad.price}
              </p>
              <div className="d-flex justify-content">
            <img src={props.ad.company_logo}
                className="img-fluid rounded-start"
                alt="..."
                style={{ maxHeight: "40px" }}
              />
            </div>
            </div>
          </div>
          </div>
        </div>
    </>
  );
}

export default AdItemRokomari;
