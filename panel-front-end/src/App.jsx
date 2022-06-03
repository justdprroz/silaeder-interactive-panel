import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, Link } from "solid-app-router";
import { onMount, createSignal } from "solid-js";

const api_url = "http://serverutl/"

const [getAchievements, setAchievements] = createSignal("");

function ReturnMenu() {
    return (
        <Link href='/'>
            <button type="button" class="fs-1 text-white btn position-absolute top-0 start-0" style="background-color:#c45a8f; margin: 5px">
                Назад
            </button>
        </Link>
    )
}

function RequestAchievements() {
    const filters = document.getElementsByClassName("filter-list");
    console.log(filters);
    for(let i = 0; i < filters.length; i++) {
        setAchievements(getAchievements() + filters[i].children[0].id + " ");
    } 
    console.log(getAchievements());
}

function Filter(props) {
    // category = ["api_key", "human-readable string"]
    // selections = [["api_key", "string"]]
    const category = props.category;
    const selections = props.selections;
    onMount(() => {
        let checkList = document.getElementById(category[0] + '-list');
        checkList.getElementsByClassName('anchor')[0].onclick = function() {
            if (checkList.classList.contains('visible'))
                checkList.classList.remove('visible');
            else
                checkList.classList.add('visible');
        }

        let buttons = document.getElementsByClassName("selection");
        for(let i = 0; i < buttons.length; i++) {
            buttons[i].onclick = function() {
                console.log(buttons[i].children[0].id);
                RequestAchievements();
            }
        }
    })
    return (
        <div id={category[0] + "-list"} class="filter-list dropdown-check-list align-top" style="margin: 5px">
            <button id={category[0]} type="button" class="anchor fs-1 text-white btn" style="background-color:#c45a8f">
                <span>{category[1]}</span>
            </button>
            <ul class="items">
                <For each={selections}>{(selection, _i) =>
                    <li>
                        <button type="button" class="selection fs-3 text-white btn w-100 d-flex justify-content-left" style="padding: 0px">
                            <input id={selection[0]} type="checkbox"/>
                            <label for={selection[0]} class="w-100 h-100 d-flex justify-content-left">
                                {selection[1]}
                            </label>
                        </button>
                    </li>
                }</For>
            </ul>
        </div>
    )
}

function MainMenu() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <div class="container text-white h-100">
                <div class="row h-50">
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/plan" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">структура школы</button>
                        </Link>
                    </div>
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/achievements" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">достижения</button>
                        </Link>
                    </div>
                </div>
                <div class="row h-50">
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/sections" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">кружки</button>
                        </Link>
                    </div>
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/facts" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">факты</button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

function Achievements() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <div id="filters" class="position-absolute top-0 end-0">
                <Filter
                    category={["category", "категория"]}
                    selections={[
                        ["olympiad", "олимпиада"],
                        ["conference", "конференция"],
                        ["sport", "спорт"]
                    ]}
                />
                <Filter
                    category={["field", "область"]}
                    selections={[
                        ["informatics", "информатика"],
                        ["math", "математика"],
                        ["economy", "экономика"]
                    ]}
                />
            </div>
            <div class="d-flex justify-content-center align-items-center h-100">
                <code>
                    {getAchievements()}
                </code>
            </div>
        </div>
    )
}

function Plan() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Plan WIP
            </h1>
        </div>
    )
}

function Sections() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Section WIP
            </h1>
        </div>
    )
}

function Facts() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Facts WIP
            </h1>
        </div>
    )
}

function App() {
    return (
        <Routes>
            <Route path="/" element={<MainMenu/>} />
            <Route path="/achievements" element={<Achievements/>} />
            <Route path="/plan" element={<Plan/>} />
            <Route path="/sections" element={<Sections/> } />
            <Route path="/facts" element={<Facts/> } />
        </Routes>
    );
}


export default App;
