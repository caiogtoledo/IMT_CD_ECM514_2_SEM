import { useState, useRef, useEffect } from "react";
import './style.css';
import { KeyboardArrowRight } from "@mui/icons-material";
import Card from "../components/Card/Card";
import ReactLoading from 'react-loading';
import { editalList } from "../data/editalList";

const SearchView = () => {
    const [text, setText] = useState("");
    const [canEnter, setCanEnter] = useState(false);
    const textareaRef = useRef(null);
    const [notices, setNotices] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const textarea = textareaRef.current;
        textarea.style.height = "auto";
        textarea.style.height = `${textarea.scrollHeight}px`;

        if (text.length === 0) {
            setCanEnter(false);
        }
        else {
            setCanEnter(true)
        }
    }, [text]);

    const handleRequest = async () => {
        setLoading(true);
        setNotices([]);

        try {
            const response = await fetch('http://localhost:8080/get-similar-notices', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: text,
                }),
            });

            if (!response.ok) {
                throw new Error('Erro ao buscar dados da API');
            }

            const data = await response.json();

            const editals = data["similar_notices"];

            let editalsFormmated = [];

            editals.forEach(item => {
                editalList.forEach(edital => {
                    console.log(edital)
                    if (edital.edital_number == item.notice) {
                        editalsFormmated.push({
                            notice: item.notice,
                            title: edital.edital_name,
                            code: item.notice,
                            link: item.document
                        });
                    }
                })
            });

            setNotices(editalsFormmated);
        } catch (error) {
            console.error('Erro na requisição:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="search">
            <p className="title-page">
                Conte-me como é o seu projeto, qual seu objetivo, desafios tecnológicos e características
            </p>
            <div className="input-button-container">
                <textarea
                    ref={textareaRef}
                    className="input"
                    placeholder="Digite aqui..."
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
                <button className="button" style={text.length ? { opacity: 1 } : { opacity: 0.8 }} disabled={!canEnter} onClick={handleRequest}>
                    <KeyboardArrowRight className="icon" />
                </button>
            </div>
            <div className="cards">
                {
                    loading ?
                        <ReactLoading type="spin" color="#fff" width={"5%"} />
                        :
                        notices?.length > 0 ?
                            notices?.map((item) => <Card code={item.code} title={item.title} distance={item.distance} link={item.link} index={item.notice} />)
                            :
                            loading && <p className="title-page" style={{ fontSize: ".9rem" }}>Sem editais encontrados</p>
                }
            </div>
        </div>
    );
};

export default SearchView;
