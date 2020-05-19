import dima from '../images/dima.jpg';
import vlad from '../images/vlad.jpg';
import vanya from '../images/vanya.jpg';
import maks from '../images/maks.jpg';

interface ITeamService {
    getData: () => object[]
}

export default class TeamService implements ITeamService {
    getData = () => {
        return [
            {
                id:1,
                name: 'Maksym Poslovskyi',
                age: 21,
                position: 'Team-Lead',
                description: 'Папин бродяга, мамин симпотяга',
                imageUrl: maks
            },

            {
                id:2,
                name: 'Gulivec Vladislav',
                age: 54,
                position: 'Senior-Python-Developur',
                description: 'Пожилая котлета',
                imageUrl: vlad
            },

            {
                id:3,
                name: 'Panshin Dima',
                age: 20,
                position: 'CEO',
                description: 'Сколько писей не триси, одна капелька в трусы',
                imageUrl: dima
            },

            {
                id:4,
                name: 'Homenko Ivan',
                age: 20,
                position: 'Creative Director',
                description: 'Люблю на тракторе бабушек возить',
                imageUrl: vanya
            }
        ]
    } 
}

